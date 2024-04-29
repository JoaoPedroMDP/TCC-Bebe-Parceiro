import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteProfessionalComponent } from './delete-professional.component';

describe('DeleteProfessionalComponent', () => {
  let component: DeleteProfessionalComponent;
  let fixture: ComponentFixture<DeleteProfessionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DeleteProfessionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DeleteProfessionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
