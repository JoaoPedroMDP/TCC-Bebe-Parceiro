import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteSpecialityComponent } from './delete-speciality.component';

describe('DeleteSpecialityComponent', () => {
  let component: DeleteSpecialityComponent;
  let fixture: ComponentFixture<DeleteSpecialityComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteSpecialityComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteSpecialityComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
