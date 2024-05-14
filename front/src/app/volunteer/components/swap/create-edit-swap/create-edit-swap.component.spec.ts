import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateEditSwapComponent } from './create-edit-swap.component';

describe('CreateEditSwapComponent', () => {
  let component: CreateEditSwapComponent;
  let fixture: ComponentFixture<CreateEditSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateEditSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateEditSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
